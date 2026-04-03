import React, { useMemo, useState } from 'react';
import styles from './NewsSection.module.css';
import { newsData } from '../../../data/newsData';

export const NewsSection = () => {
  const [page, setPage] = useState(0);
  const itemsPerPage = 2;

  const groupedNews = useMemo(() => {
    const result = [];

    for (let i = 0; i < newsData.length; i += itemsPerPage) {
      result.push(newsData.slice(i, i + itemsPerPage));
    }

    return result;
  }, []);

  const currentGroup = groupedNews[page] || [];

  const handlePrev = () => {
    setPage(prev => (prev === 0 ? groupedNews.length - 1 : prev - 1));
  };

  const handleNext = () => {
    setPage(prev => (prev === groupedNews.length - 1 ? 0 : prev + 1));
  };

  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Новини притулку:</h2>

      <div className={styles.sliderWrapper}>
        <button
          type="button"
          className={`${styles.arrow} ${styles.arrowLeft}`}
          onClick={handlePrev}
          aria-label="Попередні новини"
        >
          ←
        </button>

        <div className={styles.newsList}>
          {currentGroup.map((item, index) => (
            <article
              key={item.id}
              className={`${styles.newsCard} ${index % 2 !== 0 ? styles.reverse : ''}`}
            >
              <div className={styles.imageWrapper}>
                <img
                  src={item.image}
                  alt={item.title}
                  className={styles.image}
                />
              </div>

              <div className={styles.content}>
                <h3 className={styles.title}>{item.title}</h3>
                <p className={styles.text}>{item.text}</p>
                <span className={styles.date}>{item.date}</span>
              </div>
            </article>
          ))}
        </div>

        <button
          type="button"
          className={`${styles.arrow} ${styles.arrowRight}`}
          onClick={handleNext}
          aria-label="Наступні новини"
        >
          →
        </button>
      </div>
    </section>
  );
};
