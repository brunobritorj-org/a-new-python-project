import sys
import uuid

def main():
    version = str(uuid.uuid4())
    prefix = sys.argv[1] if len(sys.argv) > 1 else None
    if prefix:
        version = prefix + '-' + version
    print(f"'version={version}' >> $GITHUB_OUTPUT")

if __name__ == "__main__":
    main()
