import React from 'react';
import { Link } from 'react-router';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay } from 'swiper/modules';

import 'swiper/css';

import styles from './PetsSlider.module.css';

import pet1 from '../../../assets/pet1.jpeg';
import pet2 from '../../../assets/pet2.jpeg';
import pet3 from '../../../assets/pet3.jpeg';
import pet4 from '../../../assets/pet4.jpeg';
import pawButton from '../../../assets/paw-btn.svg';

const slides = [
  { id: 1, image: pet1, alt: 'pet-1' },
  { id: 2, image: pet2, alt: 'pet-2' },
  { id: 3, image: pet3, alt: 'pet-3' },
  { id: 4, image: pet4, alt: 'pet-4' },
  { id: 5, image: pet1, alt: 'pet-5' },
  { id: 6, image: pet2, alt: 'pet-6' },
];

export const PetsSlider = () => {
  return (
    <div className={styles.wrapper}>
      <Swiper
        modules={[Autoplay]}
        loop={true}
        centeredSlides={true}
        slidesPerView={3}
        spaceBetween={25}
        speed={1400}
        autoplay={{
          delay: 2100,
          disableOnInteraction: false,
          pauseOnMouseEnter: false,
        }}
        allowTouchMove={false}
        simulateTouch={false}
        className={styles.slider}
      >
        {slides.map(slide => (
          <SwiperSlide key={slide.id} className={styles.slide}>
            <img src={slide.image} alt={slide.alt} className={styles.image} />
          </SwiperSlide>
        ))}
      </Swiper>

      <Link to="/swipe" className={styles.pawLink}>
        <img src={pawButton} alt="ЛапоСвайп" className={styles.pawImage} />
      </Link>
    </div>
  );
};
