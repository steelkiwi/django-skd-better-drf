import setuptools


setuptools.setup(
    name="drf-skd-tools",
    version="0.1.2",
    author="Steelkiwi",
    author_email="dobrovolsky@steelkiwi.com",  # temp
    url="https://github.com/steelkiwi/drf-skd-tools",
    license="MIT",
    description="Steelkiwi Django Tools for DRF",
    keywords="django tools helpers",
    packages=["drf_skd_tools", "drf_skd_tools.swagger"],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'])
