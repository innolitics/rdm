FROM python:3.9.12-buster

RUN apt-get update && apt-get install -y \
    latexmk \
    texlive-fonts-recommended  \
    texlive-latex-extra \
    texlive-font-utils \
    && rm -rf /var/lib/apt/lists/*

# NOTE: replace "amd" with "arm" if compiling for arm (e.g., using a macOS M1)
RUN wget https://github.com/jgm/pandoc/releases/download/2.18/pandoc-2.18-1-arm64.deb && \
    dpkg -i pandoc-2.18-1-arm64.deb

RUN pip install rdm[github]

WORKDIR /dhf

CMD make