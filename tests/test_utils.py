import os
import pytest
from casperfpga import utils

@pytest.mark.parametrize('input_file,system_val', [('example00.fpg', 'snap_500'), ('example01.fpg', 'snap_fengine_git')])
def test_parse_fpg(shared_datadir, input_file,system_val): 
    filename = str(shared_datadir / input_file)
    meta_dictionary, memorydict = utils.parse_fpg(filename)
    assert type(meta_dictionary) is dict
    assert meta_dictionary['77777']['system'] == system_val
    
