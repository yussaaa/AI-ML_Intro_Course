import sys
print("Running from:", sys.executable)

try:
    import sklearn
    print("scikit-learn version:", sklearn.__version__)
except ImportError:
    print("scikit-learn not found")