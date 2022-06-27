import os
import pytest
from casperfpga import utils

def test_parse_example00(shared_datadir):
    """
    Test to ensure the data from snap_500.fpg is properly parsed.

    This function ensures that the two outputs of utils.parse_fpg are dictionary-like
    and return the expected meta and memory dictionary keys produced in python2.7. 
    A value from these sets is then verified.

    Parameters
    ----------
    shared_datadir : pathlib.Path object
        Injected variable that specifies the directory of where shared data is stored.
    """
    filename = str(shared_datadir / 'example00.fpg')
    meta_dictionary, memorydict = utils.parse_fpg(filename)
    meta_keys_e = {
        'snapA',
        'snap_adc', 
        'snapA_ctrl', 
        'snapA_status', 
        'snapC_ctrl', 
        'snapC_status', 
        'snapC_bram', 
        'snapA_bram', 
        'snapB_ctrl', 
        'snapC', 
        'snapB', 
        'snapB_bram', 
        'snapB_status', 
        'SNAP', 
        '77777', 
        'eth_sw', 
        '77777_git',
    }
    meta_keys_o = set(meta_dictionary.keys())
    mem_keys_e = {
        'adc16_use_synth',
        'snapC_ctrl',
        'snapA_status',
        'snapC_bram',
        'sys_scratchpad',
        'snapB_ctrl',
        'sys_rev_rcs',
        'snapC_status',
        'sys_board_id',
        'snapA_bram',
        'adc16_wb_ram0',
        'eth_sw',
        'adc16_wb_ram1',
        'lmx_ctrl',
        'adc16_wb_ram2',
        'snapA_ctrl',
        'adc16_controller',
        'sys_block',
        'snapB_status',
        'sys_rev',
        'snapB_bram',
        'sys_clkcounter'
    }
    mem_keys_o = set(memorydict.keys())
    assert meta_keys_e == meta_keys_o
    assert meta_dictionary['77777']['system'] == 'snap_500'
    assert mem_keys_e == mem_keys_o

def test_parse_example01(shared_datadir):
    """
    Test to ensure the data from snap_fengine.fpg is properly parsed.

    This function ensures that the two outputs of utils.parse_fpg are dictionary-like
    and return the expected meta and memory dictionary keys produced in python2.7. 
    A value from these sets is then verified.

    Parameters
    ----------
    shared_datadir : pathlib.Path object
        Injected variable that specifies the directory of where shared data is stored.
    """
    filename = str(shared_datadir / 'example01.fpg')
    meta_dictionary, memorydict = utils.parse_fpg(filename)
    meta_keys_e = {
        'corr_0_acc_len', 
        'timebase_sync_period', 
        'adc_snap_adc', 
        'phase_switch_gpio_switch_offset', 
        'eq_core_clip_cnt', 
        'packetizer_chans', 
        'sync_period', 
        'phase_switch_gpio_switch_states', 
        'version_version', 
        'phase_switch_sw_switch_states', 
        'corr_0_input_sel', 'eq_core_coeffs', 
        '77777', 
        'input_snap_sel', 
        'phase_switch_enable_demod', 
        'packetizer_ants', 
        'chan_reorder_reorder3_map1', 
        'eth_sw', 
        'corr_0_dout', 
        'noise_seed_1', 
        'noise_seed_0', 
        'input_snapshot', 
        'input_snapshot_status', 
        'sync_sync_delay', 
        'pfb_status', 
        'packetizer_ips', 
        'input_snapshot_ctrl', 
        'input_snapshot_bram', 
        'input_source_sel', 
        'eth_ctrl', 
        'sync_count', 
        'phase_switch_enable_mod', 
        'pfb_ctrl', 
        'corr_0_acc_cnt', 
        'sync_uptime', 
        'delay_delays', 
        'SNAP', 
        'sync_arm',
    }
    meta_keys_o = set(meta_dictionary.keys())
    mem_keys_e = { 
        'corr_0_acc_len',
        'timebase_sync_period',
        'corr_0_dout',
        'phase_switch_gpio_switch_offset',
        'eq_core_clip_cnt',
        'noise_seed_0',
        'sync_period',
        'phase_switch_gpio_switch_states',
        'version_version',
        'sys_rev_rcs',
        'delay_delays',
        'corr_0_input_sel',
        'eq_core_coeffs',
        'sys_board_id',
        'packetizer_chans', 
        'sys_block',
        'input_snap_sel',
        'phase_switch_enable_demod',
        'packetizer_ants',
        'chan_reorder_reorder3_map1',
        'eth_sw',
        'adc16_wb_ram1',
        'adc16_wb_ram0',
        'noise_seed_1',
        'adc16_wb_ram2',
        'input_snapshot_status',
        'sync_sync_delay',
        'i2c_ant2',
        'i2c_ant0',
        'i2c_ant1',
        'packetizer_ips',
        'input_snapshot_ctrl',
        'input_snapshot_bram',
        'adc16_use_synth',
        'lmx_ctrl',
        'input_source_sel',
        'sys_rev',
        'eth_ctrl',
        'sync_count',
        'sys_scratchpad',
        'phase_switch_enable_mod',
        'pfb_ctrl',
        'adc16_controller',
        'corr_0_acc_cnt',
        'sync_uptime',
        'pfb_status',
        'sys_clkcounter',
        'phase_switch_sw_switch_states',
        'sync_arm'
    }
    mem_keys_o = set(memorydict.keys())
    assert meta_keys_e == meta_keys_o
    assert meta_dictionary['77777']['system'] == 'snap_fengine_git'
    assert mem_keys_e == mem_keys_o
