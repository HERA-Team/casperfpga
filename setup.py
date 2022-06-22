from __future__ import print_function
import os
from distutils.core import setup
import glob

print("Generating casperfpga/__version__.py: ", end='')
__version__ = open('VERSION').read().strip()
print(__version__)
open('casperfpga/__version__.py','w').write('__version__="%s"'%__version__)

#read the latest git status out to an installed file
try:
    gitbranch = os.popen('git symbolic-ref -q HEAD').read().strip()
    print("Generating casperfpga/__branch__.py")
    gitlog = os.popen('git log -n1 --pretty="%h%n%s%n--%n%an%n%ae%n%ai"').read().strip()
    print("Generating casperfpga/__gitlog__.py.")
    print(gitlog)
except:
    gitbranch = "unknown branch"
    gitlog = "git log not found"
open('casperfpga/__branch__.py','w').write('__branch__ = \"%s\"'%gitbranch)
open('casperfpga/__gitlog__.py','w').write('__gitlog__ = \"\"\"%s\"\"\"'%gitlog)



setup(
    name='casperfpga',
    version=__version__,
    author='P.Prozesky',
    author_email='paulp@ska.ac.za',
    # scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='',
    license='LICENSE.txt',
    description='Talk to CASPER fpga devices using katcp or dcp.',
    long_description=open('README.txt').read(),
    install_requires=[
        'katcp',
        'numpy',
        'odict',
        'tftpy',
    ],
    extras_require = {'test': ['pytest', 'pytest-datadir']},
    provides=['casperfpga'],
    packages=['casperfpga'],  # , 'casperfpga.test'],
    package_dir={'casperfpga': 'src'},
    package_data={'' : ['LMX2581*.txt']},
    include_package_data=True,
    scripts=glob.glob('scripts/*'),
    setup_requires=['katversion'],
    use_katversion=True
)

# end
