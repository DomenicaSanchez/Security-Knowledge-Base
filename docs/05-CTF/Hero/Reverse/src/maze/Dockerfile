# If you want to run the challenge in the same condition as the server this docker file will do the trick

FROM archlinux:latest@sha256:c136b06a4f786b84c1cc0d2494fabdf9be8811d15051cd4404deb5c3dc0b2e57

RUN echo 'Server = https://archive.archlinux.org/repos/2025/11/05/$repo/os/$arch' > /etc/pacman.d/mirrorlist

# Update system and install required packages
RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm \
    llvm \
    clang \
    make \
    python \
    && pacman -Scc --noconfirm

RUN useradd -m -s /bin/bash challenge && \
    chmod 700 /home/challenge

# Set working directory
WORKDIR /home/challenge

# Create bin and src directories
RUN mkdir -p /home/challenge/bin /home/challenge/src

# Copy challenge files
COPY flag.txt /home/challenge/flag.txt
COPY Makefile /home/challenge/Makefile
COPY bin/the_maze_of_the_sorcerer.so /home/challenge/bin/the_maze_of_the_sorcerer.so
COPY src/valid_pass.c /home/challenge/src/valid_pass.c

# Set proper permissions
RUN chown -R challenge:challenge /home/challenge && \
    chmod 644 /home/challenge/flag.txt && \
    chmod 644 /home/challenge/Makefile && \
    chmod 755 /home/challenge/bin/the_maze_of_the_sorcerer.so && \
    chmod 755 /home/challenge/bin && \
    chmod 755 /home/challenge/src
