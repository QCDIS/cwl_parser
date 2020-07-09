import connexion
import six
import os
import werkzeug.utils
from swagger_server import util
from swagger_server.cwlparser import CwlParser


def parse_file(file=None):  # noqa: E501
    """send a file to parse

    Parse a file in order to extract metadata, that can be used by a planning algorithm. # noqa: E501

    :param file: 
    :type file: strstr

    :rtype: Dict
    """
    # save the cwl file
    currentdir = os.getcwd()
    file_loc = os.path.join(currentdir, "input", file.filename)
    file.save(file_loc)

    #parse the file
    parser = CwlParser(file)

    return 'do some magic!'