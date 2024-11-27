Kubernetes is an open-source container orchestration system for automating software deployment, scaling and management.
It follows a master-slave architecture for handling permissions. It has a master node that manages the cluster's control plane components: API server, etcd, scheduler and controller manager.

![[kuber.png]]

The worker nodes host the application containers and include the kubelet, container runtime, and kube-proxy to manage containers and networking.
