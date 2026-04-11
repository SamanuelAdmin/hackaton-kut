import React, { useState } from 'react';
import donateImg from '../../../assets/donate.svg';

import styles from './DonateBlock.module.css';

const amounts = [50, 100, 250, 500, 1000];

export const DonateBlock = () => {
  const [selectedAmount, setSelectedAmount] = useState(null);
  const [isCustom, setIsCustom] = useState(false);
  const [customAmount, setCustomAmount] = useState('');

  const handleSelectAmount = amount => {
    setSelectedAmount(amount);
    setIsCustom(false);
    setCustomAmount('');
  };

  const handleCustomAmount = () => {
    setSelectedAmount(null);
    setIsCustom(true);
  };

  const handleContinue = () => {
    const finalAmount = isCustom ? customAmount : selectedAmount;

    if (!finalAmount) {
      alert('Оберіть або введіть суму');
      return;
    }

    console.log('Выбрана сумма:', finalAmount);
  };

  return (
    <div className={styles.wrapper}>
      <div className={styles.left}>
        <h3 className={styles.title}>Оберіть суму разового внеску</h3>

        <div className={styles.amounts}>
          {amounts.map(amount => {
            const isActive = selectedAmount === amount && !isCustom;

            return (
              <button
                key={amount}
                type="button"
                className={`${styles.amountBtn} ${isActive ? styles.active : ''}`}
                onClick={() => handleSelectAmount(amount)}
              >
                {amount} UAH
              </button>
            );
          })}

          <button
            type="button"
            className={`${styles.amountBtn} ${isCustom ? styles.active : ''}`}
            onClick={handleCustomAmount}
          >
            Інша сума
          </button>
        </div>

        {isCustom && (
          <input
            type="number"
            min="1"
            placeholder="Введіть суму"
            value={customAmount}
            onChange={e => setCustomAmount(e.target.value)}
            className={styles.input}
          />
        )}

        <button
          type="button"
          className={styles.continueBtn}
          onClick={handleContinue}
        >
          Продовжити
        </button>
      </div>

      <div className={styles.right}>
        <img src={donateImg} alt="DonateImg" className={styles.image} />
      </div>
    </div>
  );
};
