You can use these files for manual testing of the enterprise version

### 1. Prepare workload cluster

With a workload cluster kubeconfig:

```
kubectl apply -k wc
```

### 2. Install App

Edit the `mc/kustomization.yaml` file.

Obtain a management cluster kubeconfig:

```
kubectl apply -k mc
```

### 3. Upgrade

Edit the `mc/kustomization.yaml` file. Comment in the patches

With a management cluster kubeconfig:

```
kubectl apply -k mc
```
