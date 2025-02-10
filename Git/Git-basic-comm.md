```command
git config --global user.name "John Doe"
git config --global user.email "john.doe@contoso.com"
```

You can make github proxy-aware by using:

```command
git config --global http.proxy
http://proxyUsername:proxyPassword@proxy.server.com:port
```

You can also see the logs and the current state of the commits and its hashes by:

``` command
git log
git log -n 10
```
