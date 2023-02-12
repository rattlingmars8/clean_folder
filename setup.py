from setuptools import setup, find_namespace_packages

setup(
    name= 'clean_folder',
    version= '0.0.1',
    description= 'Files organizer in some folder.',
    url='Local',
    author='rattlingmars8',
    author_email='rattlingmars8@gmail.com',
    license='None',
    packages=find_namespace_packages(),
    entry_points= {'console_scripts':['clean-folder = clean_folder.file_sorting:_sort_by_type']}
)