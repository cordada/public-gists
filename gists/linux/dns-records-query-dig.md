# Linux - DNS records - Query using dig

## TXT records

### DMARC

```bash
dig '_dmarc.google.com' TXT +short
```

```text
"v=DMARC1; p=reject; rua=mailto:mailauth-reports@google.com"
```

```bash
dig '_dmarc.bci.cl' TXT +short
```

```text
"v=DMARC1;p=reject;pct=100;fo=1;ri=86400;rua=mailto:bci_rua@dm.easysol.net;ruf=mailto:bci_ruf@dm.easysol.net"
```

```bash
dig '_dmarc.sii.cl' TXT +short
```

```text
"v=DMARC1; p=none; sp=none; rua=mailto:dmarc@sii.cl; ruf=mailto:dmarc@sii.cl;"
```
