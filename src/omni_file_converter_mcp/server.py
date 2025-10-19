import os
import sys
import time
import json
import sys
import os
import re
import codecs
import random
import logging

import os
import fitz

from typing import Deque, List, Optional, Tuple, Any, Dict
from pydantic import BaseModel
import httpx
from mcp.server.fastmcp import Context, FastMCP

logging.basicConfig(
    filename='server.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

class CustomFastMCP(FastMCP):
    async def _handle_list_tools(self, context):
        # print(f"ListTools Request Details: {context.request}")
        context.info(f"ListTools _handle_list_tools Request Details: {context.request}")
        context.info(f"ListTools _handle_list_tools Request Details: {str(context.request)}")
        return await super()._handle_list_tools(context)

# Initialize FastMCP server
server = CustomFastMCP(
    name="omni-file-converter-mcp"
)

@server.prompt("system_prompt")
def system_prompt() -> str:
    """
    """
    prompt="""
    # Omni File Converter
    The tool 
    'pdf_to_image' takes the path of your PDF file and output to Images Format. It's useful if you want to export PDF to multiple images and send to others by emails.
    """
    return prompt

@server.tool()
def pdf_to_image(
        file_path: str = "",
        output_format: str = "jpg",
        output_file_name: Optional[str] = None,
    ) -> List[Any]:
    """ Convert Your PDF Files to Various Images Formats such as JPG,PNG,JPEG, etc, with High Resolutions. 

        Args:
            file_path: Str, Local Folder Path of your Input PDF File
            output_format: Str, Supported values in upper case, include "JPG", "PNG", "JPEG", etc.
            output_file_name: The output image file name, if not specified, use the same name as input file path file_name.pdf will output  file_name_1.jpg, file_name_2.jpg, etc.
          
        Return: 
            str: json str with below values samples
            
            [
                {'output_path': '/your_local_folder/output_name_1.jpg'},
                {'output_path': '/your_local_folder/output_name_2.jpg'},
                {'output_path': '/your_local_folder/output_name_3.jpg'},
            ]
    """
    try:
        # results list of json
        result_list = convert_pdf_to_images(file_path, output_format, output_file_name)
        return result_list

    except httpx.HTTPError as e:
        return f"Error communicating with Bing Image Search API: {str(e)}"
        return []
    except Exception as e:
        return f"Unexpected error: {str(e)}"
        return []

def convert_pdf_to_images(input_path, output_format, output_folder, output_file_name: Optional[str] = None):
    """
    """
    try:

        files = input_path.split("/")
        file_name = files[-1]
        if file_name is None or file_name == "":
            return

        file_name_clean = ""
        ## e,g: a.b.c.pdf
        if file_name.endswith(".pdf"):
            file_name_clean = file_name.replace(".pdf", "")
        else:
            file_name_clean = file_name

        dpi=300
        available_format = ["JPG", "PNG"]
        if output_format.upper() not in available_format:
            return
        
        if output_file_name == "" or output_file_name is None:
            output_file_name = file_name_clean

        # Start Processing
        pdf_document = fitz.open(input_path)
        
        zoom_x=2.0
        zoom_y=2.0
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix=mat)
            image_path = os.path.join(output_folder, f'{output_file_name}_{page_num + 1}.{output_format.lower()}')
            pix.save(image_path)
        # 
        pdf_document.close()

    except Exception as e:
        print (f"Failed to Convert Pdf to Images with error {e}")
    
def test_convert_pdf_to_images():
    
    input_path = "./example.pdf"
    output_format = "jpg"
    output_folder = "./convert_output"
    convert_pdf_to_images(input_path, output_format, output_folder)

if __name__ == "__main__":
    # Initialize and run the server
    server.run(transport='stdio')
