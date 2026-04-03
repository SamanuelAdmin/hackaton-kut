import React from 'react';
import { SectionCard } from '../components/shared/SectionCard/SectionCard';
import {
  NewsSlider,
  PetsSlider,
  DonateBlock,
} from '../components/sections/index';

import img1 from '../assets/news1.jpeg';
import img2 from '../assets/news2.jpeg';
import img3 from '../assets/news3.jpeg';
import img4 from '../assets/news4.jpg';

const newsItems = [
  {
    id: 1,
    image: img1,
    title: 'Тестова новина №1',
    text: 'Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_но',
  },
  {
    id: 2,
    image: img2,
    title: 'Тестова новина №2',
    text: 'Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_но',
  },
  {
    id: 3,
    image: img3,
    title: 'Тестова новина №3',
    text: 'Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_но',
  },
  {
    id: 4,
    image: img4,
    title: 'Тестова новина №4',
    text: 'Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_новини_Текст_но',
  },
];

export const HomePage = () => {
  return (
    <>
      <SectionCard title="Новини притулку" btnText="Всі новини >" to="/news">
        <NewsSlider items={newsItems} />
      </SectionCard>
      <SectionCard
        title="Підтримати приют"
        btnText="Інша допомога >"
        to="/catalog"
      >
        <DonateBlock />
      </SectionCard>
      <SectionCard title="Знайти друга" btnText="Усі тваринки >" to="/catalog">
        <PetsSlider />
      </SectionCard>
    </>
  );
};
