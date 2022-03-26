import argparse


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--max_epoch',
        type=int,
        default=900,
        help='number of epochs of training')
    parser.add_argument(
        '--extra_steps',
        type=int,
        default=6,
        help='number of extrapolations')
    parser.add_argument(
        '--max_iter',
        type=int,
        default=50000,
        help='set the max iteration number')
    parser.add_argument(
        '-gen_bs',
        '--gen_batch_size',
        type=int,
        default=128,
        help='size of the batches')
    parser.add_argument(
        '-dis_bs',
        '--dis_batch_size',
        type=int,
        default=128,
        help='size of the batches')
    parser.add_argument(
        '--lr_g',
        type=float,
        default=0.00002,
        help='adam: gen learning rate')
    parser.add_argument(
        '--lr_d',
        type=float,
        default=0.0001,
        help='adam: disc learning rate')
    parser.add_argument(
        '--lr_decay',
        action='store_true',
        help='learning rate decay or not')
    parser.add_argument(
        '--beta1',
        type=float,
        default=-0.0,
        help='adam: decay of first order momentum of gradient')
    parser.add_argument(
        '--beta2',
        type=float,
        default=0.90,
        help='adam: decay of second order momentum of gradient')
    parser.add_argument(
        '--ema',
        type=float,
        default=0.9999,
        help='exponential moving average weights')
    parser.add_argument(
        '--num_workers',
        type=int,
        default=8,
        help='number of cpu threads to use during batch generation')
    parser.add_argument(
        '--ha_alpha',
        type=int,
        default=1.5,
        help='number of cpu threads to use during batch generation')
    parser.add_argument(
        '--ha_beta',
        type=int,
        default=0.5,
        help='number of cpu threads to use during batch generation')
    parser.add_argument(
        '--lr_r',
        type=int,
        default=2e-3,
        help='number of cpu threads to use during batch generation')
    parser.add_argument(
        '--latent_dim',
        type=int,
        default=128,
        help='dimensionality of the latent space')
    parser.add_argument(
        '--img_size',
        type=int,
        default=32,
        help='size of each image dimension')
    parser.add_argument(
        '--channels',
        type=int,
        default=3,
        help='number of image channels')
    parser.add_argument(
        '--n_critic',
        type=int,
        default=1,
        help='number of training steps for discriminator per iter')
    parser.add_argument(
        '--val_freq',
        type=int,
        default=1,
        help='interval between each validation')
    parser.add_argument(
        '--print_freq',
        type=int,
        default=300,
        help='interval between each verbose')
    parser.add_argument(
        '--load_path',
        # default='/home/zichu/PycharmProjects/best_gan/logs/cifar10_adam_2022_03_18_10_30_35',
        default='/home/zichu',
        # default='/home/zichu/PycharmProjects/Least_action_dynamics_minmax-main/ResNet/best_slead',
        type=str,
        help='The reload model path')
    parser.add_argument(
        '--alg',
        type=str,
        default='ppm',
        help='The optimization algorithm')
    parser.add_argument(
        '--exp_name',
        type=str,
        default='cifar10_adam',
        help='The name of exp')
    parser.add_argument(
        '--d_spectral_norm',
        type=str2bool,
        default=True,
        help='add spectral_norm on discriminator?')
    parser.add_argument(
        '--g_spectral_norm',
        type=str2bool,
        default=False,
        help='add spectral_norm on generator?')
    parser.add_argument(
        '--dataset',
        type=str,
        default='cifar10',
        help='dataset type')
    parser.add_argument(
        '--data_path',
        type=str,
        default='./data',
        help='The path of data set')
    parser.add_argument('--init_type', type=str, default='xavier_uniform',
                        choices=['normal', 'orth', 'xavier_uniform', 'false'],
                        help='The init type')
    parser.add_argument('--gf_dim', type=int, default=256,
                        help='The base channel num of gen')
    parser.add_argument('--df_dim', type=int, default=128,
                        help='The base channel num of disc')
    parser.add_argument(
        '--model',
        type=str,
        default='sngan_cifar10',
        help='path of model')
    parser.add_argument('--eval_batch_size', type=int, default=100)
    parser.add_argument('--num_eval_imgs', type=int, default=50000)
    parser.add_argument(
        '--bottom_width',
        type=int,
        default=4,
        help="the base resolution of the GAN")
    parser.add_argument('--random_seed', type=int, default=666)

    opt = parser.parse_args()
    return opt
