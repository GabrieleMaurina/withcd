import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='withcd',
	version='1.0.2',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='Change working directory utility compatible with with statements',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/withcd',
	licence='MIT',
	py_modules=['withcd'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
