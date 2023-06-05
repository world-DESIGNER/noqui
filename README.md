# noqui
노퀴용
# README.md

## 프로젝트 설명

이 프로젝트는 YouTube 플레이리스트에서 동영상을 다운로드하고, 오디오를 추출하여 지정한 길이와 비트레이트로 변환하는 Python 스크립트입니다. 

## 사용 기술

* Python 3

* youtube-dl

* ffmpeg

* pydub

## 필요한 지식

* 기본적인 컴퓨터 사용 능력

* 기본적인 터미널(명령 프롬프트) 사용 능력

## 시작하기 전에 

이 스크립트를 실행하려면 Python 3, pip, ffmpeg가 설치되어 있어야 합니다. 

Python이 설치되어 있지 않은 경우, [Python 공식 웹사이트](https://www.python.org/)에서 Python을 다운로드하고 설치해주세요. 

pip와 ffmpeg가 설치되어 있지 않은 경우, 아래의 명령어를 통해 설치하실 수 있습니다:

### pip 설치

```bash

python get-pip.py

```

### ffmpeg 설치

#### 윈도우:

[FFmpeg 공식 웹사이트](https://ffmpeg.org/download.html)에서 FFmpeg을 다운로드하고 설치해주세요.

#### MacOS:

```bash

brew install ffmpeg

```

#### 리눅스 (우분투):

```bash

sudo apt-get install ffmpeg

```

## 필요한 파이썬 라이브러리 설치하기

아래의 명령어를 통해 필요한 라이브러리를 설치할 수 있습니다:

```bash

pip install pydub youtube-dl

```

## 사용 방법

1. `노퀴용.py` 파일을 다운로드하거나 클론합니다.

2. 터미널을 열고 스크립트가 있는 디렉토리로 이동합니다.

3. 다음 명령어를 실행하여 스크립트를 실행합니다:

```cmd

python 노퀴용.py

```

4. 프롬프트가 나오면 추출하려는 오디오의 길이(초), 비트레이트, 전체 비디오 다운로드 여부를 입력합니다.

## 주의사항

* 이 스크립트는 개인적인 목적으로만 사용해야 합니다. 다운로드된 콘텐츠를 상업적 목적으로 사용하거나 재배포하지 마세요.

* 이 스크립트는 YouTube 서비스 약관을 위반하지 않도록 사용해야 합니다.

## 도움말

이 스크립트에 대해 궁금한 점이 있거나 문제가 발생한 경우, 이슈를 등록해주세요. 

