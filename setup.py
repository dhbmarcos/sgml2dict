from distutils.core import setup

setup(
  name             = "sgml2dict",
  packages         = ["sgml2dict"],
  version          = "0.1.1",
  license          = "MIT",
  description      = "Convert SGML text to dictionary.",
  author           = "D. H. B. Marcos",
  author_email     = "dhbmarcos@gmail.com",
  url              = "https://gitlab.com/dhbmarcos/sgml2dict",
  download_url     = "https://gitlab.com/dhbmarcos/sgml2dict/-/archive/0.0.3/sgml2dict-0.0.3.tar.gz",
  keywords         = ["SGML", "DICT", "XML", "HTML"],
  install_requires = [],
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
  ]
)