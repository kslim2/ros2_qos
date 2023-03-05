from setuptools import setup

package_name = 'learn_qos'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mike',
    maintainer_email='mike@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "qos_helloworld_pub=learn_qos.qos_helloworld_pub:main",
            "qos_helloworld_sub=learn_qos.qos_helloworld_sub:main",
        ],
    },
)
