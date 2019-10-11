import cpuinfo
from flask import jsonify


def get_processor_name():
    p = cpuinfo.get_cpu_info()['brand']

    pinfo = {"model": p}

    return jsonify(pinfo)

def get_cache(level):
    if level =='l2':
        return jsonify({'l2': cpuinfo.get_cpu_info()['l2_cache_size']})
    else:
        return jsonify({'cache': {'l2': cpuinfo.get_cpu_info()['l2_cache_size']}})
