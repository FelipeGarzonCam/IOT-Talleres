FROM python:3.9-slim


RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libgl1-mesa-dev \
    libgl1-mesa-glx \
    libglew-dev \
    libosmesa6-dev \
    libxrender1 \
    libsm6 \
    libxext6 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir pybullet numpy


WORKDIR /app


COPY two_joint_robot_custom.urdf /app/
COPY Main.py /app/


CMD ["python", "Main.py"]
