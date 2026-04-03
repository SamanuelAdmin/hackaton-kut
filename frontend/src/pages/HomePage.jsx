import React from 'react';
import { Header } from '../components/shared/Header/Header';
import { SectionCard } from '../components/shared/SectionCard/SectionCard';
import {
  NewsSlider,
  PetsSlider,
  DonateBlock,
} from '../components/sections/index';

export const HomePage = () => {
  return (
    <>
      <SectionCard title="Новини притулку" btnText="Всі новини >" to="/news">
        <NewsSlider />
      </SectionCard>
      <SectionCard title="Підтримати приют" btnText="Інша допомога >" to='/news'>
        <DonateBlock />
      </SectionCard>
      <SectionCard title="Знайти друга" btnText="Усі тваринки >" to="/catalog">
        <PetsSlider />
      </SectionCard>
    </>
  );
};
