import click
import docker
import os

client = docker.from_env()

projects = [('../Carts', 'microservice-shop-carts'), ('../Client', 'microservice-shop-client'),
            ('../Inventory', 'microservice-shop-inventory'), ('../Orders', 'microservice-shop-orders')]

docker_username = 'dethbug'


@click.group()
def cli():
    pass


@cli.command()
def build_all():
    """Docker build everything."""
    for project in projects:
        try:
            print('build started: ' + project[1])
            client.images.build(path=project[0], tag=docker_username + '/' + project[1])
            print('build finished: ' + project[1])
        except:
            print('docker build err')


@cli.command()
def push_all():
    """Upload all docker builds."""
    for project in projects:
        try:
            print('pushing: ' + docker_username + '/' + project[1])
            client.images.push(docker_username + '/' + project[1])
            print('pushing completed: ' + docker_username + '/' + project[1])
        except:
            print('docker push err')


@cli.command()
@click.pass_context
def update_images(ctx):
    """Update Images."""
    ctx.invoke(build_all)
    ctx.invoke(push_all)


@cli.command()
@click.pass_context
def helm_clean_install(ctx):
    """Install project with helm."""
    ctx.invoke(update_images)
    os.system('helm ls --all --short | xargs -L1 helm delete --purge')
    os.system("helm install ../microservice-shop-helm")


if __name__ == '__main__':
    cli()
