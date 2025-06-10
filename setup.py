from setuptools import setup, find_packages

setup(
    name="mygemini",             # pip에 등록할 이름
    version="0.1.0",                  # 패키지 버전
    description="A simple config file reader for credentials/config.ini",
    author="sniper0673",
    author_email="you@example.com",
    packages=find_packages(),         # config_reader 패키지를 자동으로 찾아줍니다
    python_requires=">=3.7",
    install_requires=[],              # 외부 의존 패키지가 있으면 여기에 리스트로 추가
    include_package_data=True,        # MANIFEST.in 등에 포함된 추가 파일도 같이 배포
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)