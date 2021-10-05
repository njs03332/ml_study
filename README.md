# nlp_study

* 추후 가상환경 생성 yaml 파일을 만들 예정. 참고: https://teddylee777.github.io/python/anaconda-가상환경설정-팁-강좌

### 1. 가상환경 생성
<details>
<summary>$ conda create --name pytorch_env python=3</summary>
<div markdown="1">

$ conda create --name pytorch_env python=3
Collecting package metadata (current_repodata.json): done
Solving environment: done

## 중간 로그 생략

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/osx-64::ca-certificates-2021.7.5-hecd8cb5_1
  certifi            pkgs/main/osx-64::certifi-2021.5.30-py39hecd8cb5_0
  libcxx             pkgs/main/osx-64::libcxx-12.0.0-h2f01273_0
  libffi             pkgs/main/osx-64::libffi-3.3-hb1e8313_2
  ncurses            pkgs/main/osx-64::ncurses-6.2-h0a44026_1
  openssl            pkgs/main/osx-64::openssl-1.1.1l-h9ed2024_0
  pip                pkgs/main/osx-64::pip-21.2.4-py37hecd8cb5_0
  python             pkgs/main/osx-64::python-3.9.7-h88f2d9e_1
  readline           pkgs/main/osx-64::readline-8.1-h9ed2024_0
  setuptools         pkgs/main/osx-64::setuptools-58.0.4-py39hecd8cb5_0
  sqlite             pkgs/main/osx-64::sqlite-3.36.0-hce871da_0
  tk                 pkgs/main/osx-64::tk-8.6.11-h7bc2e8c_0
  tzdata             pkgs/main/noarch::tzdata-2021a-h5d7bf9c_0
  wheel              pkgs/main/noarch::wheel-0.37.0-pyhd3eb1b0_1
  xz                 pkgs/main/osx-64::xz-5.2.5-h1de35cc_0
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3

## 진행 확인 동의
Proceed ([y]/n)? y


Downloading and Extracting Packages
certifi-2021.5.30    | 138 KB    | ################################################################# | 100%
tzdata-2021a         | 111 KB    | ################################################################# | 100%
readline-8.1         | 333 KB    | ################################################################# | 100%
sqlite-3.36.0        | 1.1 MB    | ################################################################# | 100%
pip-21.2.4           | 1.8 MB    | ################################################################# | 100%
ca-certificates-2021 | 113 KB    | ################################################################# | 100%
python-3.9.7         | 9.8 MB    | ################################################################# | 100%
libcxx-12.0.0        | 805 KB    | ################################################################# | 100%
wheel-0.37.0         | 33 KB     | ################################################################# | 100%
tk-8.6.11            | 3.0 MB    | ################################################################# | 100%
openssl-1.1.1l       | 2.2 MB    | ################################################################# | 100%
setuptools-58.0.4    | 792 KB    | ################################################################# | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate pytorch_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate
</div>
</details>

### 2. 가상환경 활성화
$ source activate pytorch_env

### 3. 패키지 설치
(pytorch_env) $ conda install -y pytorch-cpu torchvision-cpu -c pytorch
(pytorch_env) $ conda install jupyter notebook

### 4. ipynb 열기
(pytorch_env) $ jupyter notebook
```
[I 01:51:23.470 NotebookApp] Serving notebooks from local directory: /Users/leila/nlp_study
[I 01:51:23.470 NotebookApp] Jupyter Notebook 6.4.3 is running at:
# 생략
```