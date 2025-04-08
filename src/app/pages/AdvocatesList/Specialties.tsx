import AdvocateType, { SpecialtyType } from './types';

const Specialties = ({ specialties }: { specialties: Array<SpecialtyType>; }) => {
    if (specialties.length === 0) {
        return null;
    }
    if (specialties.length === 1) {
        return (<div>{specialties[0]}</div>);
    }
    return (
      <ul>
        {specialties.sort().map((specialty) => (
          <li key={specialty}>{specialty}</li>
        ))}
      </ul>
    );
}

export default Specialties;
