# Nginx

## Setup with local SSL

We're going to create an SSL certificate to trust websites running locally on the _.local_ top-level domain.
We can then host our applications on e.g. _myapp.local_ with Nginx as a proxy.

This means Nginx can listen on _localhost:80_ and _localhost:443_ and proxy requests to backend servers as required:
e.g. _myapp.local_ -> backend 1, _myotherapp.local_ -> backend 2. Additionally, we only need to set up Nginx with a single 
wildcard SSL certificate to cover all subdomains of _*.local_ to enable HTTPS for all our apps running locally.

### Step 1 - Create SSL Certificate

This creates an SSL certificate which secures all domains _*.local_. However, note this certificate will not be able to secure additional levels of subdomains, i.e. api.myapp.local. For this you would have to make a new certificate with the common name and SAN set to _myapp.local_. See this article on [Multi-Domain Wildcard Certificates](https://www.sslshopper.com/article-ssl-certificates-for-multi-level-subdomains.html) for more info. Alternatively, it seems you can also fix this issue by adding all the FQDNs to Subject Alternate Name (SAN). However, this requires providing every subdomain (without a wildcard) up front.

The project contains config file, _local.conf_, which defines is used to provide defaults in the command below. Create the certificate and key:

```shell
openssl req -config local.conf -new -sha256 -newkey rsa:2048 -nodes -keyout local.key -x509 -days 365 -out local.crt
```

### Step 2 - Trust the Self-Signed Certificate

Before you can use the Root SSL certificate to issue a domain certificate, you must trust the certificate on your system. This article shows how to [add trusted root certificates](https://manuals.gfi.com/en/kerio/connect/content/server-configuration/ssl-certificates/adding-trusted-root-certificates-to-the-server-1605.html) on Linux/Mac/Windows.

On Centos:

* Install ca-certificates package: `sudo yum install ca-certificates`
* Enable the dynamic CA configuration feature: `sudo update-ca-trust force-enable`
* Add it as a new file to _/etc/pki/ca-trust/source/anchors/_: `sudo cp localhost.crt /etc/pki/ca-trust/source/anchors/`
* Use command: `sudo update-ca-trust extract`

### Step 3 - Add domain to /etc/hosts

For this demo, we want to host our server on _myapp.local_. This needs to be added to _/etc/hosts_:

```text
127.0.0.1 myapp.local
```

this will route requests to the domain _myapp.local_ back to the loopback (local machine).

Note - you will to add records for all the domains you want to host. Alteratively, you could [setup a local
DNS server](https://askubuntu.com/q/743050/567843) to resolve the wildcard domain _*.local_ back to loopback.


### Step 4 - Run the Stack

We can now deploy our app:

```shell
docker-compose up -d --build
```


