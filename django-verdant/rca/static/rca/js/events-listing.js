$(function(){
	console.log(events_index);
	$('#filters input[type="radio"]').change(function() {
		// other fields are a special case - need to allow user to fill in
		//the text field
		if ($(this).val() == 'other') {
			
		} else {
			$('#listing').load(events_index, $('#filters').serialize());
			$(this).closest('li').removeClass('expanded');
			return false;
		}
	})
});