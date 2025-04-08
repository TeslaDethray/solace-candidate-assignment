import { Table as TableComponent } from 'react-bootstrap';

import TableRow from './TableRow';
import AdvocateType from './types';

const TableHead = (props) => (<th className="p-2" {...props} />);

// TODO: Issue #4 paginate the advocates
const Table = ({ advocates }: { advocates: Array<AdvocateType> }) => (
  <TableComponent striped bordered hover>
    <thead>
      <tr>
        <TableHead>First Name</TableHead>
        <TableHead>Last Name</TableHead>
        <TableHead>City</TableHead>
        <TableHead>Degree</TableHead>
        <TableHead>Specialties</TableHead>
        <TableHead>Years of Experience</TableHead>
        <TableHead>Phone Number</TableHead>
      </tr>
    </thead>
    <tbody>
      {advocates.map((advocate, index) => (
        <TableRow advocate={advocate} key={`advocate_${index}`} />
      ))}
    </tbody>
  </TableComponent>
);

export default Table;
