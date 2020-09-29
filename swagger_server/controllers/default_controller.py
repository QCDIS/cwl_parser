import connexion
import six
import os
import werkzeug.utils
from swagger_server import util
from swagger_server.cwlparser import CwlParser
import json


def parse_file(file=None):  # noqa: E501
    """send a file to parse

    Parse a file in order to extract metadata, that can be used by a planning algorithm. # noqa: E501

    :param file: 
    :type file: strstr

    :rtype: Dict
    """

    # save the cwl file
    currentdir = os.getcwd()
    input_dir = os.path.join(currentdir, "input")
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    file_loc = os.path.join(input_dir, file.filename)
    file.save(file_loc)

    #parse the file
    parser = CwlParser(file_loc)

    #set output
    metadata = {'tasks': parser.tasks, 'dependencies': parser.dependencies}

    #clear input
    os.remove(file_loc)


    #TODO: handle error codes
    return json.dumps(metadata)
