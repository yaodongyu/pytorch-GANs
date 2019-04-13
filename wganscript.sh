#!/bin/bash
python main.py --dataset mnist --gan_type WGAN --epoch 50 --batch_size 64
python main.py --dataset mnist --gan_type WGAN --epoch 800 --batch_size 1024
python main.py --dataset mnist --gan_type WGAN --epoch 3200 --batch_size 4096
python main.py --dataset cifar10 --gan_type WGAN --epoch 50 --batch_size 64
python main.py --dataset cifar10 --gan_type WGAN --epoch 800 --batch_size 1024
python main.py --dataset cifar10 --gan_type WGAN --epoch 3200 --batch_size 4096
python main.py --dataset mnist --gan_type WGAN_GP --epoch 50 --batch_size 64
python main.py --dataset mnist --gan_type WGAN_GP --epoch 800 --batch_size 1024
python main.py --dataset mnist --gan_type WGAN_GP --epoch 3200 --batch_size 4096
python main.py --dataset cifar10 --gan_type WGAN_GP --epoch 50 --batch_size 64
python main.py --dataset cifar10 --gan_type WGAN_GP --epoch 800 --batch_size 1024
python main.py --dataset cifar10 --gan_type WGAN_GP --epoch 3200 --batch_size 4096