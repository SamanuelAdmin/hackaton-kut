import React from 'react';

import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation } from 'swiper/modules';

import { Card } from '../../shared/Card/Card';

import 'swiper/css';
import 'swiper/css/navigation';

import styles from './NewsSlider.module.css';

export const NewsSlider = ({ items }) => {
  return (
    <div className={styles.sliderWrap}>
      <Swiper
        modules={[Navigation]}
        navigation
        spaceBetween={20}
        slidesPerView={'auto'}
        className={styles.slider}
      >
        {items.map(item => (
          <SwiperSlide key={item.id} className={styles.slide}>
            <Card image={item.image} title={item.title} text={item.text} />
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};
