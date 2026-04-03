import newsImg1 from '../assets/news1.jpeg';
import newsImg2 from '../assets/news2.jpeg';
import newsImg3 from '../assets/news3.jpeg';
import newsImg4 from '../assets/news4.jpg';

export const newsData = [
  {
    id: 1,
    title: 'Новина_№1',
    text: 'Тут буде текст першої новини. Поки що це мокові дані. Потім сюди можна підключити дані з бекенду.',
    date: '22:04 03.04.26',
    image: newsImg1,
  },
  {
    id: 2,
    title: 'Новина_№2',
    text: 'Тут буде текст другої новини. Цей блок також можна буде наповнювати даними із сервера.',
    date: '22:06 03.04.26',
    image: newsImg2,
  },
  {
    id: 3,
    title: 'Новина_№3',
    text: 'Третя новина для перевірки перемикання по стрілках.',
    date: '11:30 05.04.26',
    image: newsImg3,
  },
  {
    id: 4,
    title: 'Новина_№4',
    text: 'Четверта новина. Логіка побудована так, щоб перемикати одразу по дві новини.',
    date: '13:15 06.04.26',
    image: newsImg4,
  },
];
