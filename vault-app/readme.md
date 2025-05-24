Ref Doc: https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-amazon-eks

docker build -t vault-app3 .
docker run --rm   -e VAULT_TOKEN=hvs.XXXXXXXX   -e VAULT_ADDR=http://18.XX.XX.XX:30802   vault-app3
