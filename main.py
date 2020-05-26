"""
______________________________________________________________________
______________________________________________________________________

   Copyright © 2020 Alexey Skvortsov and Sergey Leshkevich

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

______________________________________________________________________
______________________________________________________________________
"""

from discord import Client, LoginFailure
import random
import asyncio
import argparse
import sys


class DSBotClient(Client):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.work = 'продаю'
        self.resourse = 'говно'
        self.channel_id = 663516107398840358
        self.end_channel_id = 709758881559085126
        self.flag = True
        self.channel = None
        self.end_channel = None

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.channel.id == self.channel_id:
            print('qq')
            if self.resourse.lower() in message.content.lower() and self.work.lower() in message.content.lower():
                self.counter += 1


async def auto_message():
    print('run!')
    try:
        client.channel_id = int(args.channel_id)
    except Exception:
        print('ID канала это число!')
        raise SystemExit
    client.counter = args.counter
    client.work = args.work_type
    client.resourse = args.resourse
    client.min_sleep = args.min_time
    client.max_sleep = args.max_time
    client.last_value = args.last_value
    client.message = ' '.join(args.extra_line)
    client.message = client.message.replace('{w}', client.work)
    client.message = client.message.replace('{r}', client.resourse)
    print('m?')
    await asyncio.sleep(5)
    print('mm?')
    client.channel = client.get_channel(client.channel_id)
    print('mmm?')
    if client.channel is None:
        print('Неверно указан ID канала')
        raise SystemExit
    print('20 seconds left')

    await asyncio.sleep(1)
    while True:
        if client.last_value > client.counter:
            raise SystemExit
        print('message sent', client.counter)
        message = client.message.replace('{c}', str(client.counter))
        await client.channel.send(message)
        time_asleep = random.randint(client.min_sleep, client.max_sleep)
        print(f'sleeping {time_asleep} seconds')
        await asyncio.sleep(time_asleep)


if __name__ == '__main__':
    client = DSBotClient()
    parser = argparse.ArgumentParser(
        description="Запуск бота, автоматизируещего добычу")
    parser.add_argument('token', type=str,
                        help='Токен вашего аккаунта')
    parser.add_argument('channel_id', type=str,
                        help='ID канала для работы')
    parser.add_argument('work_type', type=str,
                        help='Действие, выполняемое аккаунтом')
    parser.add_argument('resourse', type=str,
                        help='Ресурс/строение, исполняемое')
    parser.add_argument('counter', type=int,
                        help='Значение на момент старта скрипта')
    parser.add_argument('--min_time', type=int, default=15,
                        help='Минимальное время задержки между сообщениями(в секундах)')
    parser.add_argument('--max_time', type=int, default=30,
                        help='Максимальное время задержки между сообщениями(в секундах)')
    parser.add_argument('--last_value', type=int, default=200,
                        help='Значение, после которого скрипт прекращает работу')
    parser.add_argument('--extra_line', type=str, default=['{w}', '{r}', '{c}'],
                        help='''Вы можете создать нестандартную строку вывода сообщения в Дискорд.
                           {w} - тип работы;
                           {r} - объект работы;
                           {c} - значение, выводимое скриптом.
                        Если один из параметров будет пропущен, скрипт не запустится''',
                        nargs='*')
    args = parser.parse_args()
    print(args.extra_line)
    line = ' '.join(args.extra_line)
    if '{w}' not in line or '{r}' not in line or '{c}' not in line:
        print('Неверно задана дополнительная строка')
        raise SystemExit
    if args.min_time >= args.max_time:
        print('Минимальное время должно быть меньше максимального')
        raise SystemExit
    try:
        client.loop.create_task(auto_message())
        client.run(args.token, bot=False)
    except LoginFailure:
        print('Неверный токен')
        raise SystemExit

