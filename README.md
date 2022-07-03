# GenethicAlgorithm

Repo do algorytmu genetycznego 
Test
<img width="819" alt="image" src="https://user-images.githubusercontent.com/28493310/176255864-8eb27916-4ed7-41be-bccf-23ea73ebbb0e.png">




Łączymy nasze środowisko z AWS jak w instrukcji 
https://4sysops.com/archives/install-boto3-aws-sdk-for-python-in-visual-studio-code-vs-code-on-windows/

* zamaist plilków można uruchomić aws confugure i podać klucze z IAM


## Instalacja dockera

W celu zbudowania obrazu potrzebujemy na macu aplikcajci Docker. Poradnik jak wykonać instlację pod adresem:

https://www.raywenderlich.com/9159-docker-on-macos-getting-started


## Przykłady 

```docker
- docker pull [image]
- docker images or docker image ls
- docker ps -a or docker container ls -a
- docker ps -a -q -f [filter condition]
- docker exec -it [container] bash
- docker stop [container]
- docker start [container]
- docker rm $(docker ps -a -q -f status=exited)
- docker rm $(docker stop $(docker ps -q))
- docker rm [container IDs or names] 
- docker rmi [image] or docker image rm [image]
- docker container inspect [container]
- docker network create [network-name]
- docker network inspect [network-name]
- docker network ls
- docker network prune
- docker volume create [volume-name]
- docker volume inspect [volume-name]
- docker volume ls
- docker volume prune
- docker cp [container:container-path] [host-path]
- docker cp [host-path] [container:container-path] 

```




