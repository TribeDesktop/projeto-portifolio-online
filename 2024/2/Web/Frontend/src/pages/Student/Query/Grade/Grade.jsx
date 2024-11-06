import styles from './Grade.module.css';
import Menu from '../../../../components/Student/Menu/Menu';
import icons from '../../../../assets/images/icons/icons';
import Panel from '../../../../components/Panel/Panel';

const Grades = () => {
  return (
    <div className={styles.gradesContainer}>
      <Menu studentName={'Ana Clara'} />
      <div className={styles.gradesSideContent}>
        <Panel pageName="Painel do Aluno" section="Consultas/Notas" color="#677C91" />

        <div className={styles.gradesInfo}>
          <div className={styles.gradesCard}>
            <div className={styles.gradesCardTitle}>
              <p>Notas</p>
              <hr />
            </div>

            <div className={styles.gradesCardTable}>
              <div className={styles.gradesCardTableHeader}>
                <div className={styles.gradesHeader}>
                  <span>Média</span>
                  <span>Atividade</span>
                  <span>Nota</span>
                </div>
              </div>

              <div className={styles.gradesCardTableBody}>
                <div className={styles.gradesBody}>
                  <div className={styles.gradesDropdownBody}>
                    <span>Nome da materia</span>
                    <span>Geral</span>
                    <span>9.5</span>
                    <img src={icons.arrowDown.src} alt={icons.arrowDown.src} />
                  </div>

                  <div className={styles.gradesDropdownBody}>
                    <span>Nome da materia</span>
                    <span>Geral</span>
                    <span>9.5</span>
                    <img src={icons.arrowDown.src} alt={icons.arrowDown.src} />
                  </div>

                  <div className={styles.gradesDropdownBody}>
                    <span>Nome da materia</span>
                    <span>Geral</span>
                    <span>9.5</span>
                    <img src={icons.arrowDown.src} alt={icons.arrowDown.src} />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Grades;
