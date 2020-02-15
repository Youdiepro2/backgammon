const url = '/ajax';
const MESSAGE_DIV_ID = '#messages';
const GAME_WINNED_KEY = 'game_winned';
const CAN_MOVE_CLASS = 'canMove';
const MOVE_TO_THIS_FIELD_CLASS = 'move_to_this_field';

function post(json){
    $.ajax({
      url: url,
      type: 'POST',
      dataType:'json',
      contentType: 'application/json',
      data:JSON.stringify(json),
      success: (game) => renderGame(game),
      error: (err, s , exception) => console.log(exception),
  });
}

$(document).ready(function(){
    post({'cmd':'init'});
});

function renderGame(game) {
	console.log(game);
	$(MESSAGE_DIV_ID).empty();
	renderWinner(game);
	renderFields(game);
  renderBar(game);
  selectMoves(game);
	// renderErrors(game);
}

function renderBar(game){
  $('#field0').empty();
  $('#field25').empty();
  game.pawns.pawns.filter(
    pawn => pawn.fieldId == 0 || pawn.fieldId == 25
  ).forEach(pawn => {
      const fieldId = createFieldId(pawn.fieldId);
      $(fieldId).append(createPawnHTML(pawn))
  });

}

function renderWinner(game) {
	if (game.winner !== null) {
		const translatedError = `<p class='success'>${translate(GAME_WINNED_KEY, pl)}${game.winner._value_}</p>`;
		if (translatedError !== null) {
			$(MESSAGE_DIV_ID).append(translatedError);
		}
	}
}

function renderErrors(game){
	const errors = game.violations.messages;
	errors.forEach((error) => {
		const translatedError = `<p class='error'>${translate(error, pl)}</p>`;
		if (translatedError !== null) {
			$(MESSAGE_DIV_ID).append(translatedError);
		}
	});
}

function renderFields(game) {
  const moves = game.moves.moves;
  const fields = game.fields.fields;
	fields.forEach((field) => {
		const id = createFieldId(field.id);
		$(id).empty();
		$(id).off('click');

    field.pawns.pawns.forEach((pawn) => {
      $(id).append(createPawnHTML(pawn));
	   });
  });
}

function selectMoves(game) {
  const fields = game.fields.fields;
  const moves = game.moves.moves;
  const pawns = game.pawns.pawns;
  removeMovesSelect(game);
  pawns.forEach(pawn => {
    const pawnMoves = moves.filter((move) => move.pawnId == pawn.id);
    if (pawnMoves.length){
      const pawnId = createPawnId(pawn.id);
      $(pawnId).addClass(CAN_MOVE_CLASS);
      $(pawnId).bind('click',() => selectPawnMoves(game, pawnMoves));
    }
  });
}

function selectPawnMoves(game, pawnMoves) {
  removeMovesSelect(game);
  pawnMoves.forEach(move => {
    const fieldId = createFieldId(move.fieldId);
    const pawnId = createPawnId(move.pawnId);
    $(pawnId).addClass(CAN_MOVE_CLASS);
    $(fieldId).addClass(MOVE_TO_THIS_FIELD_CLASS);
    $(pawnId).bind('click',() => renderGame(game));
    $(fieldId).bind('click',() => post(move));
  });
}

function removeMovesSelect(game) {
  const fields = game.fields.fields;
  fields.forEach(field => {

    const fieldId = createFieldId(field.id);
    $(fieldId).off('click');
    $(fieldId).removeClass(MOVE_TO_THIS_FIELD_CLASS);

    field.pawns.pawns.forEach(pawn => {
      const pawnId = createPawnId(pawn.id);
      $(pawnId).off('click');
      $(pawnId).removeClass(CAN_MOVE_CLASS);
    });

  });
}

function createPawnHTML(pawn) {
  return `<div id="pawn${pawn.id}" class="pawn pawn__${pawn.color}">${pawn.id}</div>`
}

function createPawnId(pawnId) {
  return `#pawn${pawnId}`;
}

function createFieldId(fieldId){
	return `#field${fieldId}`;
}

function translate(key, object) {
	return object[key] || null;
}

const pl = {
	'cant_mark_inactive_board': 'Nie możesz zaznaczyć nieaktywnej planszy!',
	'field_already_marked': 'Nie możesz zaznaczyć już zaznaczonego pola!',
	'field_out_of_board': 'Zarządano zaznaczenia pola z poza planszy',
	'no_such_board': 'Nie ma planszy o tym id',
	'board_already_winned': 'Nie możesz zaznaczyć już wygranej planszy, zaznacz dowolną inną',
	'game_winned': 'Grę wygrywa '
};
