import React from 'react';
import styles from './HelpSection.module.css';

import { DonateBlock } from '../DonateBlock/DonateBlock';
import { SectionCard } from '../../shared/SectionCard/SectionCard';
import { Button } from '../../ui/Button';
import { helpData } from '../../../data/helpData';

export const HelpSection = () => {
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Допомога притулку:</h2>

      <div className={styles.helpCard}>
        <div className={styles.imageWrapper}>
          <img
            src={helpData.image}
            alt={helpData.title}
            className={styles.image}
          />
        </div>

        <div className={styles.content}>
          <h3 className={styles.title}>{helpData.title}</h3>
          <p className={styles.text}>{helpData.text}</p>

          <div className={styles.buttonWrapper}>
            <Button>{helpData.buttonText}</Button>
          </div>
        </div>
      </div>
      <SectionCard>
        <DonateBlock />
      </SectionCard>
    </section>
  );
};
