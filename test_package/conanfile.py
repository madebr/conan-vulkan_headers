# -*- coding: utf-8 -*-

from conans import ConanFile, CMake
import os


class VulkanHeadersTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        os.path.isfile(os.path.join(self.deps_user_info["vulkan_headers"].VULKAN_REGISTRY_PATH, "vk.xml"))

