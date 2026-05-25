import os

CF_HANDLE = os.environ["CF_HANDLE"]
CF_API_KEY = os.environ["CF_API_KEY"]
CF_API_SECRET = os.environ["CF_API_SECRET"]
GH_TOKEN = os.environ["GH_TOKEN"]
GH_REPO = os.environ["GH_REPO"]

SUBMISSIONS_DIR = "submissions"

LANG_EXT = {
  "gnu g++20 11.2.0 (64 bit)":           "cpp",
    "gnu g++17 7.3.0":                   "cpp",
    "gnu g++17 9.2.0 (64 bit, msys 2)":  "cpp",
    "gnu g++14 6.4.0":                   "cpp",
    "clang++17 diagnostics":             "cpp",
    "python 3.8.3":                      "py",
    "python 3.11 (64)":                  "py",
    "pypy 3.9.10 (64bit)":               "py",
    "java 17 64bit":                     "java",
    "java 11 64bit":                     "java",
    "java 8 32bit":                      "java",
    "kotlin 1.7":                        "kt",
    "javascript v8 4.8.0":               "js",
    "c# 10":                             "cs",
    "go 1.19.5":                         "go",
    "rust 2021":                         "rs",
}