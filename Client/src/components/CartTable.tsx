import React from "react";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

function ccyFormat(num: number) {
  return `${num.toFixed(2)}`;
}

function priceRow(qty: number, unit: number) {
  return qty * unit;
}

function createRow(id: number, desc: string, qty: number, unit: number) {
  const price = priceRow(qty, unit);
  return { id, desc, qty, unit, price };
}

function subtotal(items: ItemRow[]) {
  return items.map(({ price }) => price).reduce((sum, i) => sum + i, 0);
}

interface ItemRow {
  desc: string;
  qty: number;
  unit: number;
  price: number;
}
interface Item {
  name: string;
  price: number;
  amount: number;
}

interface Props {
  items: Item[];
}
function SpanningTable(props: Props) {
  const rows = props.items.map((item, id) =>
    createRow(id, item.name, item.amount, item.price)
  );
  const invoiceSubtotal = subtotal(rows);
  return (
    <Paper>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Desc</TableCell>
            <TableCell align="right">Qty.</TableCell>
            <TableCell align="right">@</TableCell>
            <TableCell align="right">Price</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.id}>
              <TableCell>{row.desc}</TableCell>
              <TableCell align="right">{row.qty}</TableCell>
              <TableCell align="right">${ccyFormat(row.unit)}</TableCell>
              <TableCell align="right">${ccyFormat(row.price)}</TableCell>
            </TableRow>
          ))}
          <TableRow>
            <TableCell rowSpan={3} />
            <TableCell colSpan={2}>Total</TableCell>
            <TableCell align="right">${ccyFormat(invoiceSubtotal)}</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </Paper>
  );
}

export default SpanningTable;
