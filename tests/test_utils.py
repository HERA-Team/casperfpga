import os
import pytest
from casperfpga import utils

def test_parse_example00(shared_datadir):
    filename = str(shared_datadir / 'example00.fpg')
    meta_dictionary, memorydict = utils.parse_fpg(filename)
    keys = {
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
    meta_keys = set(meta_dictionary.keys())
    assert meta_keys == keys

def test_parse_example01(shared_datadir):
    filename = str(shared_datadir / 'example01.fpg')
    meta_dictionary, memorydict = utils.parse_fpg(filename)
    keys = {
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
    meta_keys = set(meta_dictionary.keys())
    assert meta_keys == keys

