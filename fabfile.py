from fabric import Connection


def hello_world():
    with Connection("ubuntu@52.204.68.47") as c:
        result = c.run('echo "Hello, world!"')
        print(result.stdout)


if __name__ == "__main__":
    hello_world()
