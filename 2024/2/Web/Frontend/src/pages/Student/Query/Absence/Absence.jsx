import styles from './Absence.module.css';
import Menu from '../../../../components/Student/Menu/Menu';
import Panel from '../../../../components/Panel/Panel';

const Absence = () => {
  return (
    <div className={styles.absenceContainer}>
      <Menu studentName={'Ana Clara'} />
      <div className={styles.absenceSideContent}>
        <Panel pageName="Painel do Aluno" section="Consultas/Faltas" color="#677C91" />
        <div className={styles.absenceInfo}>
          <div className={styles.absenceCard}>
            <div className={styles.absenceCardTitle}>
              <p>Faltas</p>
              <hr />
            </div>
            <div className={styles.absenceCardSubject}>
              <span>Disciplina: </span>
              <select name="subject">
                <option value="disciplina">Selecione uma Disciplina</option>
                <option value="disciplina">disciplina</option>
              </select>
            </div>
            <div className={styles.absenceCardTable}>
              <div className={styles.absenceCardTableHeader}>
                <div className={styles.absenceHeader}>
                  <h1>Matéria</h1>
                  <h1 className={styles.absenceHeaderAcronym}>Sigla</h1>
                  <h1 className={styles.absenceHeaderTotalClasses}>Total aulas</h1>
                  <h1>Total faltas</h1>
                </div>
              </div>

              <div className={styles.absenceCardTableBody}>
                <div className={styles.absenceBody}>
                  <h2>Nome da matéria</h2>
                  <h2>Sigla</h2>
                  <h2>18 aulas</h2>
                  <h2>2 faltas</h2>
                  <hr />
                </div>
                <div className={styles.absenceBody}>
                  <h2>Nome da matéria</h2>
                  <h2>Sigla</h2>
                  <h2>18 aulas</h2>
                  <h2>2 faltas</h2>
                  <hr />
                </div>
                <div className={styles.absenceBody}>
                  <h2>Nome da matéria</h2>
                  <h2>Sigla</h2>
                  <h2>18 aulas</h2>
                  <h2>2 faltas</h2>
                  <hr />
                </div>
                <div className={styles.absenceBody}>
                  <h2>Nome da matéria</h2>
                  <h2>Sigla</h2>
                  <h2>18 aulas</h2>
                  <h2>2 faltas</h2>
                  <hr />
                </div>
                <div className={styles.absenceBody}>
                  <h2>Nome da matéria</h2>
                  <h2>Sigla</h2>
                  <h2>18 aulas</h2>
                  <h2>2 faltas</h2>
                  <hr />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Absence;
