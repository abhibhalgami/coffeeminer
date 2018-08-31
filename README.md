# CoffeeMiner
# Original repo https://github.com/arnaucode/coffeeMiner
# Edited by : Abhi Bhalgami

Collaborative (mitm) cryptocurrency mining pool in wifi networks

**Warning: this project is for academic/research purposes only.**

A blog post about this project can be read here: http://arnaucode.com/blog/coffeeminer-hacking-wifi-cryptocurrency-miner.html

![coffeeMiner](https://raw.githubusercontent.com/arnaucode/coffeeMiner/master/coffeeMiner-logo-small.png "coffeeMiner")

## Concept
- Performs a MITM attack to all selected victims
- Injects a js script in all the HTML pages requested by the victims
- The js script injected contains a cryptocurrency miner
- All the devices victims connected to the Lan network, will be mining for the CoffeeMiner


## Use
- install.sh
```
bash install.sh
```

- execute run
```
sudo ./run eth0
```
- here replace ```eth0``` with ```wlan0``` if you want to perform in wifi

![network](https://raw.githubusercontent.com/arnaucode/coffeeMiner/master/coffeeMiner-network-attack.png "network")



![demo](https://raw.githubusercontent.com/arnaucode/coffeeMiner/master/coffeeMiner-demo-cutted.gif "demo")
