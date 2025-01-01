FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_HOME=/opt/android-sdk
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV ANDROID_AVD_HOME=/root/.android/avd
ENV PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    git \
    python3 \
    python3-pip \
    openjdk-17-jdk \
    nodejs \
    npm \
    usbutils \
    && rm -rf /var/lib/apt/lists/*

# Install Android SDK
RUN mkdir -p ${ANDROID_HOME} && cd ${ANDROID_HOME} \
    && wget https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip \
    && unzip commandlinetools-linux-*.zip \
    && rm commandlinetools-linux-*.zip \
    && mkdir -p cmdline-tools/latest \
    && mv cmdline-tools/* cmdline-tools/latest/ || true \
    && mv cmdline-tools/latest cmdline-tools/ \
    && mkdir -p ${ANDROID_HOME}/licenses \
    && echo "24333f8a63b6825ea9c5514f83c2829b004d1fee" > ${ANDROID_HOME}/licenses/android-sdk-license \
    && echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> ${ANDROID_HOME}/licenses/android-sdk-license \
    && echo "y" | ${ANDROID_HOME}/cmdline-tools/latest/bin/sdkmanager --licenses \
    && ${ANDROID_HOME}/cmdline-tools/latest/bin/sdkmanager \
        "platform-tools" \
        "platforms;android-30" \
        "build-tools;30.0.3" \
        "system-images;android-30;google_apis;x86_64" \
        "emulator"

# Create AVD directory
RUN mkdir -p ${ANDROID_AVD_HOME}

# Update PATH to include Android tools
ENV PATH=${PATH}:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools

# Install Appium
RUN npm install -g appium@2.0.0 \
    && npm install -g appium-uiautomator2-driver

# Create virtual device
RUN echo "no" | avdmanager create avd -n test_avd -k "system-images;android-30;google_apis;x86_64"

# Set up Python environment
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

# Copy test files
COPY . /app/

# Install additional tools for emulator
RUN apt-get update && apt-get install -y \
    qemu-kvm \
    libvirt-daemon-system \
    libvirt-clients \
    bridge-utils

# Start Appium and run tests
CMD ["python3", "-m", "tests.start_appium.py"] 