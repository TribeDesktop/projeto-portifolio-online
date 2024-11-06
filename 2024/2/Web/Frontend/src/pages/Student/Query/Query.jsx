import styles from './Query.module.css';
import Menu from '../../../components/Student/Menu/Menu';
import icons from '../../../assets/images/icons/icons';
import Panel from '../../../components/Panel/Panel';

const Query = () => {
  return (
    <div className={styles.queryContainer}>
      <Menu studentName={'Ana Clara'} />
      <div className={styles.querySideContent}>
        <Panel pageName="Painel do Aluno" section="Consultas" color="#677C91" />
        <div className={styles.queryInfo}>
          <div className={styles.queryTitle}>
            <p className={styles.queryTitleText}>Consultas</p>
          </div>
          <div className={styles.queryCard}>
            <div className={styles.cardTitles}>
              <p>Faltas</p>
              <img src={icons.arrowLeft.src} alt={icons.arrowLeft.alt} />
            </div>
            <div className={styles.cardContent}>
              <p>Cheque suas faltas durante o semestre ou toda sua jornada acadêmica.</p>
            </div>
          </div>
          <div className={styles.queryCard}>
            <div className={styles.cardTitles}>
              <p>Notas</p>
              <img src={icons.arrowLeft.src} alt={icons.arrowLeft.alt} />
            </div>
            <div className={styles.cardContent}>
              <p>Cheque suas notas durante o semestre ou toda sua jornada acadêmica.</p>
            </div>
          </div>
          <div className={styles.queryCard}>
            <div className={styles.cardTitles}>
              <p>Aulas</p>
              <img src={icons.arrowLeft.src} alt={icons.arrowLeft.alt} />
            </div>
            <div className={styles.cardContent}>
              <p>Cheque suas aulas de todo o curso e todo seu histórico de matérias.</p>
            </div>
          </div>
          <div className={styles.queryCard}>
            <div className={styles.cardTitles}>
              <p>Histórico</p>
              <img src={icons.arrowLeft.src} alt={icons.arrowLeft.alt} />
            </div>
            <div className={styles.cardContent}>
              <p>Cheque todo seu histórico da faculdade até hoje, de notas e faltas.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Query;
